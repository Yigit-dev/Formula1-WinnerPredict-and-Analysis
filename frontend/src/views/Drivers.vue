<template>
  <section>
    <Loading v-if="loading"/>
    <Table v-if="!loading" :data="data" :tableData="tableData" title="Drivers"/>
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
      tableData: ["Pos","Driver","Nationality","Car","PTS","Year"]
    }
  },
  async created() {
    await this.$appAxios.get("/drivers")
      .then(response => this.data = Object.values(response.data)[0].drivers)
      .then(this.loading = !this.loading)
      .catch(error => console.log(error))
  },
}
</script>

<style scoped>


</style>