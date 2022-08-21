<template>
  <div>
    <p style="background-color: red">This is a web component.</p>
    <p v-if="cid">cid: {{cid}}</p>
    <p v-else>No cid</p>
  </div>
</template>

<script>
export default {
  name: "MyWebComp",
  props: ['cid']
}
</script>

<style scoped>

</style>