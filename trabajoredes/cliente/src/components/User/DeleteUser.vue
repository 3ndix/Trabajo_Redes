<template lang="html">
    <div class="container">
      <div class="row">
        <div class="col">

          <h3>¿Estas seguro que deseas eliminar este usuario?</h3>
          <p>Rut : {{this.element.rut}}</p>
          <p>Nombres : {{ this.element.nombres }}</p>
          <p>Appellido Paterno : {{this.element.ap_paterno}}</p>
          <p>Appellido Materno : {{this.element.ap_materno}}</p>
          <p>Género : {{this.element.genero}}</p>

        </div>
      </div>
      <div class="row">
        <div class="col">
          <b-button v-on:click="DeleteUser" variant="danger">Eliminar</b-button>
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
      element: {
        rut: '',
        nombres: '',
        ap_paterno: '',
        ap_materno: '',
        genero: ''
      }
    }
  },
  methods: {
    getUser () {
      const path = 'http://localhost:8000/api/v1.0/users/'+this.userId+'/'

      axios.get(path).then((response) => {
        this.element.rut = response.data.rut
        this.element.nombres = response.data.nombres
        this.element.ap_paterno = response.data.ap_paterno
        this.element.ap_materno = response.data.ap_materno
        this.element.genero = response.data.genero
      })
      .catch((response) => {
        console.log(error)
      })
    },
    DeleteUser () {
      const path = 'http://localhost:8000/api/v1.0/users/'+this.userId+'/'

      axios.delete(path).then((response) => {
        location.href = '/users'
      })
      .catch((error) => {
        swal("No es posible eliminar el libro", "", "error")
      })
    }
  },
  created() {
    this.getUser()
  }
}
</script>

<style lang="css" scoped>
</style>
