/* eslint-disable */
import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Streadsheet from '@/components/Streadsheet';


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/hello/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/',
      name: 'Streadsheet',
      component: Streadsheet
    }
  ]
})
