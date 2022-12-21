<template>
<div>
    <h1>{{title}}</h1>
    <div class="actions">
        <button @click="exportCSV" id="btnExportToCsv" type="button" class="button">Export to CSV</button>
        <button @click="exportJSON" id="btnExportToCsv" type="button" class="button">Export to JSON</button>
    </div>
    <table id="dataTable">
        <tr>
            <th v-for="(item,index) in tableData" :key="index" >{{ item }}</th>
        </tr>

        <tr v-for="(data,index) in data" :key="index">
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
        tableData: {type: Array, required: true}
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
            const jsonString = `data:text/json;chatset=utf-8,${encodeURIComponent(JSON.stringify(this.data))}`;
            const link = document.createElement("a");
            link.href = jsonString;
            link.download = `${this.title}.json`;
            link.click();
        }
    }
}
</script>

<style scoped>
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