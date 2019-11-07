<template>
  <main>
    <h1>Login</h1>
    <input type="text" v-model="email" placeholder="E-mail" />
    <br />
    <input type="password" v-model="password" placeholder="Password" />
    <br />
    <div class="btn-login">
      <button @click="login">Sign in</button>
    </div>
    <p>
      Don't have an account yet?
      <router-link to="/signup">Create an account</router-link>
    </p>
  </main>
</template>
<script>
import firebase from "firebase/app";
import "firebase/auth";

export default {
  data() {
    return {
      email: null,
      password: null
    };
  },
  methods: {
    login: async function() {
      try {
        const user = await firebase
          .auth()
          .signInWithEmailAndPassword(this.email, this.password);
        this.$router.replace("home");
        console.log("User logged in:", user);
      } catch (ex) {
        console.error("Fail on login. Error: ", ex);
        alert(`Fail on login. Error:  ${ex}`);
      }
    }
  }
};
</script>