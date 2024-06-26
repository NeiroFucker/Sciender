import { createRouter, createWebHistory } from "vue-router";

const routes = [
    {
        path: "",
        redirect: { name: "login" }
    }
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
