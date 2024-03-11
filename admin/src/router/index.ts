import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		{
			path: "/",
			redirect: "/dashboard/homepage",
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
				{
					path: "dataview",
					name: "dataview",
					component: () => import("@/views/Empty.vue"),
				},
				{
					path: "notification",
					name: "notification",
					component: () => import("@/views/Empty.vue"),
				},
				{
					path: "setting",
					name: "setting",
					component: () => import("@/views/Empty.vue"),
				},
			],
		},
	],
});

export default router;
