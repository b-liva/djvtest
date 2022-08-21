<template>
  <div>
    <p>{{ msg }}...!</p>
    <div>
      <ul>
        <div v-if="continentsLoading" style="background-color: #2c3e50; color: white">loading</div>
        <li v-for="cn in continents" :key="cn.name">{{ cn.name }}</li>
        *********************************************************
        <div v-if="countriesLoading" style="background-color: #2c3e50; color: white">loading</div>
        <li v-for="country in countries" :key="country.name">{{ country.name }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import {useQuery} from '@vue/apollo-composable'
import {getCountries, getContinents} from "../graphql/query/country.graphql";
import {computed} from "vue";

export default {
  setup() {
    const {result: continentsResult, error: continentsError, loading: continentsLoading} = useQuery(getContinents);
    const continents = computed(() => continentsResult.value?.continents ?? [])
    const {result: countriesResult, error: countriesError, loading: countriesLoading} = useQuery(getCountries);
    const countries = computed(() => countriesResult.value?.countries ?? [])
    return {
      continentsLoading,
      countriesLoading,
      countries,
      continents
    }
  },
  name: "Mine",
  data() {
    return {
      msg: 'hello there',
    }
  }
}
</script>

<style scoped>

</style>