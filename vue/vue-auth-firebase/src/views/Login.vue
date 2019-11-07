<template>
  <main>
    <h1>Login</h1>
    <div class="input-group mb-3">
      <input type="text" class="form-control" v-model="email" placeholder="E-mail" />
      <input type="password" class="form-control" v-model="password" placeholder="Password" />
      <br />
      <button class="btn btn-secondary" @click="loginWithEmailPassword">Sign in</button>
    </div>
    <div>or</div>
    <div>
      <button class="btn btn-primary" @click="loginWithGoogle">Sign in with Google</button>
    </div>
    <br />
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
    loginWithEmailPassword: async function() {
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
    },
    loginWithGoogle: async function() {
      try {
        const provider = new firebase.auth.GoogleAuthProvider();
        const user = await firebase.auth().signInWithPopup(provider);
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