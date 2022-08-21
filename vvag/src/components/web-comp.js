import {ApolloClient, createHttpLink, InMemoryCache} from "@apollo/client/core";
import {provideApolloClient} from '@vue/apollo-composable'

import {defineCustomElement} from 'vue'
import MyWebComp from "./MyWebComp.ce.vue";
import Mine from "./Mine.ce.vue";


const httpLink = createHttpLink({
    // You should use an absolute URL here
    uri: 'https://countries.trevorblades.com/',
})


// Cache implementation
const cache = new InMemoryCache()
const apolloClient = new ApolloClient({
    link: httpLink,
    cache,
})
provideApolloClient((apolloClient));


const MyWebElement = defineCustomElement(MyWebComp);
const MineElement = defineCustomElement(Mine);

export {MyWebElement, MineElement}

//register
export function register() {
    customElements.define('myweb-element', MyWebElement);
    customElements.define('mine-element', MineElement);
}
register();