# ecommerce_oracle_database
GRANT ALL PRIVILEGES TO ECOMMERCE;
sudo lsof -t -i tcp:8000
sudo kill -9 -tpc
uvicorn main:app --reload --env-file .env