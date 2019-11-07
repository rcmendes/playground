<template>
  <main>
    <h1>Login</h1>
    <input type="text" name="email" placeholder="E-mail" />
    <br />
    <input type="password" name="password" placeholder="Password" />
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
export default {
  data() {
    return {};
  },
  methods: {
    login: function() {
      this.$router.replace("home");
    }
  }
};
</script>