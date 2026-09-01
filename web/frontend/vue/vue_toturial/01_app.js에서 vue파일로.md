해당 프로젝트에서 components를 만들고  
그안에 component로 만들 파일을 만들어준다. 예제 이름은 Accordion.vue

그리고 src 디렉토리의 app.js 파일은 원래 이런식이였는데 
```js
// import Vue from 'vue';
import Vue from 'vue/dist/vue.js';

Vue.component('accordion', {
    props: ['item'],
    
    template: `
        <div>
            <p> env1: {{ env1 }} </p>
            <p> env2: {{ env2 }} </p>
        </div>
        `,

    data: function() {
        return {
            toggle: true,
            env1: process.env.MIX_ROS_BRIDGE_ADDRESS,
            env2: "hello env"
        }
    }
            
});

new Vue({
    el: '#app',

    data: {
        items: [
            { id: 1, title: 'title11', description: 'Description for 11'},
            { id: 2, title: 'title22', description: 'Description for 22'},
        ], 
        env1: process.env.VUE_APP_ROS_BRIDGE_ADDRESS,
        env2: 'hello env'
    }
    
});
```

여기에서 component와 template 부분을 떼어내서 Accordion.vue 파일로 가져간다  

```vue
<template>
    <div>
        <p> env1: {{ env1 }} </p>
        <p> env2: {{ env2 }} </p>
    </div>
</template>

<script>
    export default {
        name: "Accordion",

        props: ['item'],

        data: function() {
            return {
                toggle: true,
                env1: process.env.MIX_ROS_BRIDGE_ADDRESS,
                env2: "hello env"
            }
        }
    }
</script>

<!-- <style scoped>
</style> -->
```

after app.js 파일에는 Vue.componet() 부분이 없어지고, 대신에 새로만든 컴포넌트 Accordion.vue 파일을 import한다   
그리고 Vue.component()로 사용했던 부분이 없어지고, Vue 로 만드는 부분에서 직접 components로 등록해주게 됨
```js
// import Vue from 'vue';
import Vue from 'vue/dist/vue.js';
import Accordion from './components/Accordion.vue';

new Vue({
    el: '#app',

    components: {
        Accordion,
    },

    data: {
        items: [
            { id: 1, title: 'title11', description: 'Description for 11'},
            { id: 2, title: 'title22', description: 'Description for 22'},
        ], 
        env1: process.env.VUE_APP_ROS_BRIDGE_ADDRESS,
        env2: 'hello env'
    }
    
});
```