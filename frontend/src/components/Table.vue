<template>
<div>
    <h1>Table</h1>
    <table>
        <tr>
            <th>Test COL</th>
            <th>Test COL</th>
            <th>Test COL</th>
            <th>Test COL</th>
        </tr>
        <tr>
            <td data-th="test-1">Test 1</td>
            <td data-th="test-2">Test 2</td>
            <td data-th="test-3">Test 3</td>
            <td data-th="test-4">Test 4</td>
        </tr>
        <tr>
            <td data-th="test-1">Test 1</td>
            <td data-th="test-2">Test 2</td>
            <td data-th="test-3">Test 3</td>
            <td data-th="test-4">Test 4</td>
        </tr>
        <tr>
            <td data-th="test-1">Test 1</td>
            <td data-th="test-2">Test 2</td>
            <td data-th="test-3">Test 3</td>
            <td data-th="test-4">Test 4</td>
        </tr>
        <tr>
            <td data-th="test-1">Test 1</td>
            <td data-th="test-2">Test 2</td>
            <td data-th="test-3">Test 3</td>
            <td data-th="test-4">Test 4</td>
        </tr>
    </table>
</div>
</template>
<script>
export default {
    name: "Table",
}
</script>
<style scoped>
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
    font-size: 1.25rem;
}
table td {
    display: block;
    font-size: 1.15rem;
}
table td:first-child {
    padding-top: 0.5em;
}
table td:last-child {
    padding-bottom: 0.5em;
}
table td:before {
    content: attr(data-th) ": ";
    font-weight: bold;
    width: 6.5em;
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