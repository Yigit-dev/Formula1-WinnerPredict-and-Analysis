<template>
  <section>
    <Loading v-if="loading"/>
    <Table v-if="!loading" :data="data" :tableData="tableData" :searchFilter="searchFilter" title="Formula 1"/>
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
      tableData: ["Grand Prix","Date","Winner","Car","Laps","Country","weather","weather_warm","weather_cold","weather_dry","weather_wet","weather_cloudy"],
      searchFilter: [
        {name: "Grand Prix", checked: true},
        {name: "Car"},
        {name: "Winner"}
      ]
    }
  },
  async created() {
    await this.$appAxios.get("/formula1")
      .then(response => this.data = Object.values(response.data)[0].formula1)
      .then(this.loading = !this.loading)
      .catch(error => console.log(error))
  },

}
</script>