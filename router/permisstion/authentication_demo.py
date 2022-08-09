# import os
# from typing import Tuple
#
# import jwt
# from fastapi.security.utils import get_authorization_scheme_param
# from jwt import ExpiredSignatureError, DecodeError, InvalidTokenError
# from starlette.authentication import AuthenticationError, AuthCredentials, UnauthenticatedUser, BaseUser
# from starlette.middleware.authentication import AuthenticationMiddleware
# from starlette.requests import Request, HTTPConnection
# from starlette.responses import Response, PlainTextResponse
# from starlette.types import Scope, Receive, Send
#
# from router.permisstion.user_auth import UserAuth
#
#
# class AuthenticationMiddlewareExtended(AuthenticationMiddleware):
#
#     async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
#         if scope["type"] not in ["http"]:
#             await self.app(scope, receive, send)
#             return
#
#         conn = Request(scope)
#         try:
#             auth_result = await self.authenticate(conn)
#         except AuthenticationError as exc:
#             response = self.raise_error(conn, exc)
#             if scope["type"] == "http":
#                 await response(scope, receive, send)
#             return
#         if auth_result is None:
#             auth_result = AuthCredentials(), UnauthenticatedUser()
#         scope["auth"], scope["user"] = auth_result
#         await self.app(scope, receive, send)
#
#     async def authenticate(self, request: Request
#                            ) -> Tuple[AuthCredentials, BaseUser]:
#         scheme, credential = get_authorization_scheme_param(request.headers.get(
#             "Authorization"))
#         if scheme == "Bearer":
#             try:
#                 token_decoded = jwt.decode(credential, key=os.getenv('SECRET_KEY'), algorithms="HS256")
#                 return AuthCredentials(), UserAuth(username=token_decoded.get("sub"))
#             except ExpiredSignatureError:
#                 raise AuthenticationError("signature expired")
#             except InvalidTokenError:
#                 raise AuthenticationError("token invalid")
#
#     @staticmethod
#     def raise_error(conn: HTTPConnection, exc: Exception) -> Response:
#         return PlainTextResponse(str(exc), status_code=401)
