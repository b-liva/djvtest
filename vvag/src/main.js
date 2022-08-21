// Add this at the beginning of your app entry.
// alert('hi there');
import {register} from './components/web-comp.js';
import 'vite/modulepreload-polyfill';
import { createApp, provide, h } from 'vue'
import App from './App.vue'
import {ApolloClient, createHttpLink, InMemoryCache} from '@apollo/client/core'
import { DefaultApolloClient, provideApolloClient } from '@vue/apollo-composable'
// HTTP connection to the API
const httpLink = createHttpLink({
    // You should use an absolute URL here
    uri: 'https://countries.trevorblades.com/',
})

// Cache implementation
const cache = new InMemoryCache()

// Create the apollo client
const apolloClient = new ApolloClient({
    link: httpLink,
    cache,
});
provideApolloClient(apolloClient)
const app = createApp({
  setup () {
    provide(DefaultApolloClient, apolloClient)
  },

  render: () => h(App),
})
app.mount("#app");