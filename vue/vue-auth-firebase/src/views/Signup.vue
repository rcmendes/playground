<template>
  <div class="sign-up">
    <h1>Create an Account</h1>
    <input v-model="email" placeholder="E-mail" />
    <br />
    <input type="password" v-model="password" placeholder="Password" />
    <br />
    <button @click="onSignup">Create</button>
    <span>
      or return to
      <router-link to="/login">login page</router-link>
    </span>
  </div>
</template>
<script>
import firebase from "firebase";

export default {
  data: () => ({
    email: "",
    password: ""
  }),
  methods: {
    onSignup: async function() {
      try {
        const user = await firebase
          .auth()
          .createUserWithEmailAndPassword(this.email, this.password);
        this.$router.replace("home");
        console.log("Created user:", user);
      } catch (ex) {
        console.error("Fail on create account. Error: ", ex);
        alert("Fail on create account. Error: ", ex);
      }
    }
  }
};
</script>