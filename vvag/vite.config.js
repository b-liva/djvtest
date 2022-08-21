import {fileURLToPath, URL} from 'node:url'
const { resolve } = require('path');
import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue';
import graphql from '@rollup/plugin-graphql';

// https://vitejs.dev/config/
export default defineConfig({
    root: resolve('./src'),
    base: '/static/',
    server: {
        host: 'localhost',
        port: 3000,
        open: false,
        watch: {
            usePolling: true,
            disableGlobbing: false
        }
    },
    plugins: [vue({
        template: {
            compilerOptions: {
                // treat all tags with a dash as custom elements
                isCustomElement: (tag) => tag.includes('-')
            }
        }
    }), graphql()],
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        },
        extensions: ['.js', '.json']
    },
    build: {
        // outDir: "../static/src/jvf/dist/",
        outDir: resolve('../static/src/vvag/dist/'),
        assetsDir: '',
        manifest: true,
        emptyOutDir: true,
        lib: {
            entry: './src/components/web-comp.js',
            formats: ['es', 'cjs'],
            name: "vue-web-comp",
            fileName: format => (format === "es" ? "index.js" : "index.cjs.js")
        },
        sourcemap: true,
        target: 'es2015',
        minify: false,
        rollupOptions: {
            output: {
                chunkFileNames: undefined,
            },
            input: {
                main: resolve('./src/main.js')
            }
        }
    },
    define: {
        'process.env': {}
    }
})
