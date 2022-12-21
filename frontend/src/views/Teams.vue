<template>
  <section>
    <Loading v-if="loading"/>
    <Table v-if="!loading" :data="data" :tableData="tableData" title="Teams"/>
  </section>
</template>

<script>
import Table from '../components/Table.vue'
import Loading from '../icons/Loading.vue'

export default {
  components: { Table, Loading },
  name: 'HomeView',
  data(){
    return{
      data: [],
      loading: true,
      tableData: ["Pos","Team","PTS","Year"]
    }
  },
  async created() {
    await this.$appAxios.get("/teams")
      .then(response => this.data = Object.values(response.data)[0].teams)
      .then(this.loading = !this.loading)
      .catch(error => console.log(error))
  },
}
</script>

<style scoped>


</style>