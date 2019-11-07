import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import firebase from "firebase";

Vue.config.productionTip = false;

var firebaseConfig = {
	apiKey: "AIzaSyAd_lo8mt2H2ESCG5WEe9SnCopDEmqKilo",
	authDomain: "dev-vue-auth-firebase.firebaseapp.com",
	databaseURL: "https://dev-vue-auth-firebase.firebaseio.com",
	projectId: "dev-vue-auth-firebase",
	storageBucket: "dev-vue-auth-firebase.appspot.com",
	messagingSenderId: "715823289035",
	appId: "1:715823289035:web:72758249c872153ef5414e",
	measurementId: "G-3RW6E24VJE"
};

firebase.initializeApp(firebaseConfig);
firebase.analytics();

// let app = null;
// firebase.auth().onAuthStateChanged(() => {
// 	if (!app) {
// 		app = new Vue({
// 			router,
// 			render: h => h(App)
// 		}).$mount("#app");
// 	}
// });

new Vue({
	router,
	render: h => h(App)
}).$mount("#app");
