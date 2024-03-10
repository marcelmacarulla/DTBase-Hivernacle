# backend API base URL, used by frontend, ingress, and model functions.
CONST_BACKEND_URL = os.environ.get("DT_BACKEND_URL", "http://localhost:5000")

DEFAULT_USER_EMAIL = "default_user@localhost"
DEFAULT_USER_PASS = os.environ.get("DT_DEFAULT_USER_PASS", None)
