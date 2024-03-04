import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		{
			path: "/",
			redirect: "/dashboard",
		},
		{
			path: "/dashboard",
			name: "dashbord",
			component: () => import("@/views/Dashboard.vue"),
			children: [
				{
					path: "homepage",
					name: "homepage",
					component: () => import("@/views/Dashboard/HomePage.vue"),
				},
				{
					path: "students",
					name: "students",
					component: () => import("@/views/Dashboard/Students.vue"),
				},
			],
		},
	],
});

export default router;
