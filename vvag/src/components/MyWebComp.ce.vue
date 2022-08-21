<template>
  <div>
    <p style="background-color: red">This is a web component.</p>
    <p v-if="book">last book: <span class="book">{{book}}</span> from <span class="author">{{author}}</span></p>
    <p v-else>No books available</p>
  </div>
</template>

<script>
export default {
  name: "MyWebComp",
  props: ['book', 'author']
}
</script>

<style scoped>
.book{
  color: crimson;
}
.author{
  color: white;
  background-color: #2c3e50;
  border-radius: 5px;
  padding: 5px;
}
</style>