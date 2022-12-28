<template>
<div>
    <h1>{{title}}</h1>
    <div class="search">
        <input type="text" class="search" v-model="search">
        <div class="searchFilter">
            <label v-for="(item,index) in this.searchFilter" :key="index">
                <input type="radio" :id="item.name" :value="item.name" v-model="filter" :checked="item.checked ? true : false"/>
                <span>{{ item.name }}</span>
            </label>
        </div>
    </div>
    <div class="actions">
        <button @click="exportCSV" id="btnExportToCsv" type="button" class="button">Export to CSV</button>
        <button @click="exportJSON" id="btnExportToCsv" type="button" class="button">Export to JSON</button>
    </div>
    <table id="dataTable">
        <tr>
            <th @click="sort('Date')" v-for="(item,index) in tableData" :key="index" >{{ item }}</th>
        </tr>

        <tr v-for="(data,index) in filteredItems" :key="index">
            <td v-for="(item,index) in tableData" :key="index" :data-th="index">{{ data[item] }}</td>
        </tr>
    </table>
</div>
</template>

<script>
import {TableCSVExporter} from "../utils/TableCSVExporter"
export default {
    name: "Table",
    props: {
        data: {type: Array, required: true},
        title: {type: String},
        tableData: {type: Array, required: true},
        searchFilter: {type: Array, required: true}
    },
    data(){
        return{
            search: '',
            filter: this.searchFilter.filter(item => item.checked)[0].name
        }
    },
    methods:{
        sort(props){
            this.data.sort((a,b) => a[props] > b[props] ? -1 : 1 || a[props] < b[props] ? -1 : 1 )
        },
        exportCSV(){
            const dataTable = document.getElementById("dataTable");
            const exporter = new TableCSVExporter(dataTable);
            const csvOutput = exporter.convertToCSV();
            const csvBlob = new Blob([csvOutput], { type: "text/csv" });
            const blobUrl = URL.createObjectURL(csvBlob);
            const anchorElement = document.createElement("a");

            anchorElement.href = blobUrl;
            anchorElement.download = `${this.title}.csv`;
            anchorElement.click();
            setTimeout(() => {
                URL.revokeObjectURL(blobUrl);
            }, 500);
        },
        exportJSON(){
            const jsonString = `data:text/json;chatset=utf-8,${encodeURIComponent(JSON.stringify(this.filteredItems))}`;
            const link = document.createElement("a");
            link.href = jsonString;
            link.download = `${this.title}.json`;
            link.click();
        }
    },
    computed: {
        filteredItems () {
            return this.data.filter(item => {
                let filter = this.filter !== '' ? this.filter : 'Grand Prix';
                return item[filter].toLowerCase().indexOf(this.search.toLowerCase()) > -1
            })
        }
    }
}
</script>

<style scoped>
.search{
    display: flex;
    justify-content: flex-start;
    align-items: center;
}
.search input.search {
  width: 240px;
  padding: 10px 45px;
  background: var(--c-secondary) url("../assets/search.svg") no-repeat 16px center;
  background-size: 16px 16px;
  font-size: 14px;
  border: none;
  border-radius: 5px;
  color: #fff;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
    margin-right: 6px;
}
.searchFilter{
    display: flex;
}
label {
	 display: flex;
	 cursor: pointer;
	 font-weight: 500;
	 position: relative;
	 overflow: hidden;
}
label input {
	 position: absolute;
	 left: -9999px;
}
label input:checked + span {
	 background-color: var(--c-secondary);
}
label input:checked + span:before {
	 color: var(--c-formula1);
}
label span {
	 display: flex;
	 align-items: center;
	 padding: 0.375em 0.75em 0.375em 0.375em;
	 border-radius: 99em;
	 transition: 0.25s ease;
}
label span:hover {
	 background-color: var(--c-secondary);
}
label span:before {
	 display: flex;
	 flex-shrink: 0;
	 content: "";
	 background-color: var(--c-primary);
	 width: 1.5em;
	 height: 1.5em;
	 border-radius: 50%;
	 margin-right: 0.375em;
	 transition: 0.25s ease;
	 box-shadow: inset 0 0 0 0.125em var(--c-formula1);
}
 
.actions{
    display: flex;
    justify-content: flex-end;
    align-items: center;
}
.actions > *:not(:last-child) {
    margin-right: 16px;
}
.actions button{
    padding: 8px 12px;
    border-radius: 6px;
    background: var(--c-secondary);
    color: #fff;
    transition: all 300ms;
}
.actions button:hover{
    background: var(--c-primary);
    transition: all 300ms;
}
table {
    width: 100%;
    margin: 1em 0;
    min-width: 300px;
}
table tr {
    border-top: 1px solid #ddd;
    border-bottom: 1px solid #ddd;
}
table tr:nth-child(2n+1) td:nth-child(n+1){
    background: #323245;
}
table th {
    display: none;
    font-weight: 700;
    font-size: 1.1rem;
    cursor: pointer;
}
table th:hover{
    background: var(--c-formula1);
    color: #fff;
}
table td {
    display: block;
    text-align: center;
    font-size: 1rem;
}
table td:first-child {
    padding-top: 0.3em;
}
table td:last-child {
    padding-bottom: 0.3em;
}
table td:before {
    content: attr(data-th) ": ";
    font-weight: bold;
    width: 5em;
    display: inline-block;
}
@media (min-width: 480px) {
    table td:before {
        display: none;
	}
}
 table th, table td {
    text-align: left;
}
@media (min-width: 480px) {
    table th, table td {
        display: table-cell;
        padding: 0.25em 0.5em;
	}
    table th:first-child, table td:first-child {
        padding-left: 0;
	}
    table th:last-child, table td:last-child {
        padding-right: 0;
	}
}


table {
    background: var(--c-primary);
    color: #fff;
    border-radius: .8em;
    overflow: hidden;
}
table tr {
	border-color: #46637f;
}
table  tr:not(:first-child):hover{
    background: var(--c-secondary);
}
table th, table td {
    margin: 0.5em 1em;
}
 @media (min-width: 480px) {
    table th, table td {
        padding: 1em !important;
	}
}
table th, table td:before {
    color: var(--c-formula1);
}
</style>