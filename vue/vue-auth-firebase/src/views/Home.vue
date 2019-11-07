<template>
  <div class="home">
    <h1>Vue Authentication with Firebase!!!</h1>
    <h4>{{currentUser.email}}</h4>
    <button @click="sair">Sair</button>
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