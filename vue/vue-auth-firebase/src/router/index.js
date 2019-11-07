import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";
import About from "@/views/About.vue";
import Login from "@/views/Login.vue";
import SignUp from "@/views/SignUp.vue";
import firebase from "firebase/app";
import "firebase/auth";

Vue.use(VueRouter);

const routes = [
	{
		path: "*",
		redirect: "/login"
	},
	{
		path: "/",
		redirect: "/login"
	},
	{
		path: "/home",
		component: Home,
		meta: {
			requiresAuth: true
		}
	},
	{
		path: "/about",
		component: About
	},
	{
		path: "/login",
		component: Login
	},
	{
		path: "/signup",
		component: SignUp
	}
];

const router = new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes
});

router.beforeEach((to, from, next) => {
	const currentUser = firebase.auth().currentUser;
	const requiresMatch = to.matched.some(record => record.meta.requiresAuth);

	if (requiresMatch && !currentUser) {
		next("login");
	} else if (!requiresMatch && currentUser) {
		next("home");
	} else {
		next();
	}
});

export default router;
