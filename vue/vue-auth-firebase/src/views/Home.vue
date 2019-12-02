<template>
  <div class="home">
    <h1>Hello !!!</h1>
    <h3>{{currentUser.displayName}}</h3>
    <h5>{{currentUser.email}}</h5>
    <button class="btn btn-primary" @click="sair">Sair</button>
  </div>
</template>

<script>
import firebase from "firebase/app";
import "firebase/auth";

export default {
  methods: {
    sair: function() {
      firebase
        .auth()
        .signOut()
        .then(() => {
          this.$router.replace("login");
        });
    }
  },
  computed: {
    currentUser: () => firebase.auth().currentUser
  }
};
</script>