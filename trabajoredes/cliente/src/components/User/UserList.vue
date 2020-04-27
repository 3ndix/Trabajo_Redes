<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <div class="">
          <h2>Listado de usuarios</h2>
          <br>
          <b-button size="sm" :to="{name: 'NewUser'}" variant="primary">
            Nuevo usuario
          </b-button>
        </div>
        <br>
        <div class="col-md-12">
          <b-table striped hover :items="users" :fields="fields">
            <template v-slot:cell(action)="data">
              <b-button size="sm" variant="primary" :to="{ name: 'VerUser', params: {userId: data.item.id} }">
                Ver
              </b-button>
              <b-button size="sm" variant="primary" :to="{ name: 'EditUser', params: {userId: data.item.id} }">
                Editar
              </b-button>
            </template>
          </b-table>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import swal from 'sweetalert'
export default {
    data () {
      return {
        userId: this.$route.params.userId,
        fields: [
          { key: 'nombres', label: 'Nombres' },
          { key: 'ap_paterno', label: 'Apellido Paterno' },
          { key: 'ap_materno', label: 'Apellido Materno' },
          { key: 'action', label: '' }
        ],
        users: []
      }
    },

    methods: {
      getUsers () {

        const path = 'http://localhost:8000/api/v1.0/users/'
        axios.get(path).then((response) => {
          this.users = response.data
        })
        .catch((error) => {
          console.log(error)
        })
      },
    },
    created(){
      this.getUsers()
    },
  }
</script>

<style lang="css" scoped>

</style>
