<template>
  <section>
    <Loading v-if="loading"/>
    <Table v-if="!loading" :data="data" :tableData="tableData" title="Races"/>
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
      tableData: ["Grand Prix","Date","Winner","Car","Laps", "Time", "Year", "Day", "Month"]
    }
  },
  async created() {
    await this.$appAxios.get("/races")
      .then(response => this.data = Object.values(response.data)[0].races)
      .then(this.loading = !this.loading)
      .catch(error => console.log(error))
  },
}
</script>

<style scoped>


</style>