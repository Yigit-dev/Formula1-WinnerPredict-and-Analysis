<template>
    <div class="tables">
        <ul>
            <li><router-link to="/">Formula 1</router-link></li>
            <li><router-link to="/drivers">Drivers</router-link></li>
            <li><router-link to="/teams">Teams</router-link></li>
            <li><router-link to="/races">Races</router-link></li>
        </ul>
    </div>
</template>
<script>
export default {
    name: 'TableNavigation'   
}
</script>
<style scoped>
ul{
    display: flex;
    justify-content: center;
    align-items: center;
}
ul li {
    list-style: none;
}

ul li a{
    color: #fff;
}
ul li:not(:last-child){
    margin-right: 18px;
}
    
</style>