<template>
  <v-app>
    <Layout>
      <router-view/>
    </Layout>
  </v-app>
</template>

<script>
import Layout from './components/Layout/index.vue';

export default {
    name: "App",
    components: { Layout }
}
</script>
