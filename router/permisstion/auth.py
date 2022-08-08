import os
import typing
from datetime import datetime, timedelta

import jwt
from fastapi.security.utils import get_authorization_scheme_param
from jwt import ExpiredSignatureError, InvalidTokenError
from starlette.authentication import (
    AuthCredentials,
    AuthenticationBackend,
    AuthenticationError,
    UnauthenticatedUser, BaseUser,
)
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.requests import HTTPConnection, Request
from starlette.responses import PlainTextResponse, Response
from starlette.types import ASGIApp, Receive, Scope, Send
from schema import Token
from router.permisstion.user_auth import UserAuth





class AuthenticationMiddlewareExtended(AuthenticationMiddleware):
    def __init__(self, app: ASGIApp, backend: AuthenticationBackend, on_error: typing.Callable[
        [HTTPConnection, AuthenticationError], Response
    ] = None) -> None:
        super().__init__(app, backend, on_error)
        self.app = app
        self.on_error: typing.Callable[
            [HTTPConnection, AuthenticationError], Response
        ] = (on_error if on_error is not None else self.default_on_error)

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] not in ["http", "websocket"]:
            await self.app(scope, receive, send)
            return

        conn = Request(scope)
        try:
            auth_result = await self.authenticate(conn)
        except AuthenticationError as exc:
            response = self.on_error(conn, exc)
            if scope["type"] == "websocket":
                await send({"type": "websocket.close", "code": 1000})
            else:
                await response(scope, receive, send)
            return

        if auth_result is None:
            auth_result = AuthCredentials(), UnauthenticatedUser()
        scope["auth"], scope["user"] = auth_result
        await self.app(scope, receive, send)

    async def authenticate(self, request: Request) -> typing.Tuple[AuthCredentials, BaseUser]:
        scheme, credential = get_authorization_scheme_param(request.headers.get("Authorization"))
        if scheme == "Bearer":
            try:
                token_decoded = jwt.decode(credential, key=os.getenv('SECRET_KEY'), algorithms=os.getenv('ALGORITHM'))
                return AuthCredentials(), UserAuth(username=token_decoded.get("sub"))
            except ExpiredSignatureError:
                raise AuthenticationError("signature expired")
            except InvalidTokenError:
                raise AuthenticationError("token invalid")


    @staticmethod
    def default_on_error(conn: HTTPConnection, exc: Exception) -> Response:
        return PlainTextResponse(str(exc), status_code=400)