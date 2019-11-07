<template>
  <div class="home">
    <h1>Vue Authentication with Firebase!!!</h1>
    <button @click="sair">Sair</button>
  </div>
</template>

<script>
import firebase from "firebase";

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
  }
};
</script>