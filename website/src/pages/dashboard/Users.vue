<template>
  <div class='q-pa-md'>
    <q-table :data='dataTableUsers' :columns='columnsTableUsers' row-key="name" />
  </div>
</template>

<script>
import { mapActions } from 'vuex';
import * as typesUser from '../../store/users/types';

export default {
  name: 'PageUsers',
  data: () => ({
    columnsTableUsers: [
      {
        name: 'username',
        align: 'center',
        label: 'Username',
        field: 'username',
        sortable: false,
      },
      {
        name: 'email',
        align: 'center',
        label: 'Email',
        field: 'email',
        sortable: false,
      },
    ],
    dataTableUsers: [],
  }),
  mounted() {
    this.loadDataUsers();
  },
  methods: {
    ...mapActions({
      loadDataUsers: typesUser.LOAD_USERS,
    }),
  },
};
</script>
