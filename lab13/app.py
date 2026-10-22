import streamlit as st
import hashlib
import hmac

st.set_page_config(page_title="PostgreSQL Auth Demo")
st.title("Lab 13: Login / Signup with PostgreSQL")
st.warning("Configure PostgreSQL credentials in .streamlit/secrets.toml before using database features.")

try:
    import psycopg2
    from psycopg2.extras import RealDictCursor
    import bcrypt
except ImportError:
    st.error("Dependencies are missing. Run: python -m pip install -r ../requirements.txt")
    st.stop()

try:
    database_url = st.secrets["postgres"]["url"]
except Exception:
    st.info(
        "Create a local file named .streamlit/secrets.toml in the project root with:\n\n"
        '[postgres]\nurl = "postgresql://USER:PASSWORD@HOST:5432/DATABASE?sslmode=require"\n\n'
        "Use a PostgreSQL database you control. Do not commit secrets.toml to GitHub."
    )
    st.stop()

def get_connection():
    return psycopg2.connect(database_url, connect_timeout=5)

def initialize_db():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    password_hash VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

try:
    initialize_db()
except Exception as exc:
    st.error(f"Could not connect to PostgreSQL or initialize table: {exc}")
    st.stop()

mode = st.radio("Choose action", ["Sign up", "Log in"], horizontal=True)
with st.form("auth_form"):
    username = st.text_input("Username")
    email = st.text_input("Email") if mode == "Sign up" else ""
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button(mode)

if submit:
    if not username.strip() or not password:
        st.error("Username and password are required.")
    elif mode == "Sign up" and not email.strip():
        st.error("Email is required.")
    else:
        try:
            with get_connection() as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    if mode == "Sign up":
                        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                        cur.execute(
                            "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
                            (username.strip(), email.strip(), password_hash)
                        )
                        st.success("Account created. You can now log in.")
                    else:
                        cur.execute(
                            "SELECT username, password_hash FROM users WHERE username = %s",
                            (username.strip(),)
                        )
                        user = cur.fetchone()
                        if user and bcrypt.checkpw(password.encode(), user["password_hash"].encode()):
                            st.session_state["logged_in_user"] = user["username"]
                            st.success(f"Welcome, {user['username']}!")
                        else:
                            st.error("Invalid username or password.")
        except psycopg2.errors.UniqueViolation:
            st.error("That username or email already exists.")
        except Exception as exc:
            st.error(f"Database operation failed: {exc}")

if st.session_state.get("logged_in_user"):
    st.success(f"Logged in as {st.session_state['logged_in_user']}")
    if st.button("Log out"):
        del st.session_state["logged_in_user"]
        st.rerun()
