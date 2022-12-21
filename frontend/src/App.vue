<template>
    <Layout>
      <router-view/>
    </Layout>
</template>

<script>
import Layout from './components/Layout/index.vue';

export default {
    name: "App",
    components: { Layout }
}
</script>
