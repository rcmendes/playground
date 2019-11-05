<template>
  <main>
    <h1>Login</h1>
    <input type="text" name="email" placeholder="E-mail" />
    <br />
    <input type="password" name="password" placeholder="Password" />
    <br />
    <div class="btn-login">
      <button>Sign in</button>
    </div>
    <p>
      Don't have an account yet?
      <a href="#">Create an account</a>
    </p>
  </main>
</template>
<script>
export default {
  data: () => ({})
};
</script>