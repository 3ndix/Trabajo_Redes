import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import UserList from '@/components/User/UserList'
import EditUser from '@/components/User/EditUser'
import DeleteUser from '@/components/User/DeleteUser'
import NewUser from '@/components/User/NewUser'
import SaludoUser from '@/components/User/SaludoUser'
import VerUser from '@/components/User/VerUser'



Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/users',
      name: 'UserList',
      component: UserList
    },
    {
      path: '/users/:userId/edit',
      name: 'EditUser',
      component: EditUser
    },
    {
      path: '/users/new',
      name: 'NewUser',
      component: NewUser
    },
    {
      path: '/users/:userId/datos',
      name: 'VerUser',
      component: VerUser
    }
  ],
  mode: 'history'
})
