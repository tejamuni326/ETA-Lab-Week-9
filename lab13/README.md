Lab 13 — Login/Signup with PostgreSQL.

This app requires a PostgreSQL database and credentials. Set secrets locally in
`.streamlit/secrets.toml` (do not commit it). The app displays setup instructions
if credentials are missing. For a real deployment, configure Streamlit secrets.

Required secrets:
[postgres]
url = "postgresql://USER:PASSWORD@HOST:5432/DATABASE?sslmode=require"
