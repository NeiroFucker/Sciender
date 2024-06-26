export const TOKEN_NAME = "sciender-token";
export const PERMISSION_NAME = "sciender-permission";
export const ID_NAME = "sciender-id";

export const USER_PERMISSION = "ScienderUser";
export const ADMIN_PERMISSION = "Admin";

export const STUDENT_USER = "ScienderStudent";
export const GRADUATE_USER = "ScienderGraduateStudent";
export const SCIENCE_TUTOR = "ScienderScienceTutor";
export const SCIENCE_WORKER = "ScienderScienceWorker";

export const BASE_URL = "http://127.0.0.1:8000/sciender-api/v1/";

export const USER_IMAGE_URL = "core/image";
export const USER_CARD_URL = "match/user_cards";
export const LOGIN_ROOT = "token/login";
export const CREATE_MATCH = "match/create";
export const USER_INFO = (id) => `profile/${id}/info`;
export const PROJECTS_INFO = (id) => `profile/${id}/projects`;
export const PROJECT_DETAIL = (id) => `projects/${id}/detail`;
export const TO_USER_PREMATCH = "match/prematch/to_user";
export const FROM_USER_PREMATCH = "match/prematch/from_user";
export const USER_MATCH = "match/";
export const USER_CHATS = "chats/"