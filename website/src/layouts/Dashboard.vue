<template>
  <q-layout view="lHh Lpr lff">
    <q-header elevated class="bg-cyan-8">
      <q-toolbar>
        <q-btn flat @click="drawer = !drawer" round dense icon="menu" />
        <q-toolbar-title>{{ titleApp }}</q-toolbar-title>
        <q-btn flat round dense icon="notifications">
          <q-badge color="red" floating>4</q-badge>
        </q-btn>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="drawer" :width="280" :breakpoint="400" show-if-above>
      <q-scroll-area
        style="height: calc(100% - 150px); margin-top: 150px; border-right: 1px solid #ddd"
      >
        <q-list padding>
          <q-item clickable v-ripple v-for="(item, key) in itemsMenu" :key="key" :to="item.to">
            <q-item-section avatar>
              <q-icon :name="item.icon"/>
            </q-item-section>

            <q-item-section>{{item.title}}</q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>

      <q-img
        class="absolute-top"
        src="https://cdn.quasar.dev/img/material.png"
        style="height: 150px"
      >
        <div class="absolute-bottom bg-transparent">
          <q-avatar size="56px" class="q-mb-sm">
            <img src="https://cdn.quasar.dev/img/boy-avatar.png" />
          </q-avatar>
          <div class="text-weight-bold">Razvan Stoenescu</div>
          <div>@rstoenescu</div>
        </div>
      </q-img>
    </q-drawer>

    <q-page-container>
      <q-space />
      <div class="q-pa-md q-gutter-sm">
        <q-breadcrumbs>
          <q-breadcrumbs-el icon="home" to="/" />
          <q-breadcrumbs-el label="Dashboard" icon="widgets" to="/start/pick-quasar-flavour" />
          <q-breadcrumbs-el label="Users" icon="people" to="/vue-components/breadcrumbs" />
        </q-breadcrumbs>
      </div>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'LayoutDashboard',
  data: () => ({
    drawer: true,
    itemsMenu: [
      {
        title: 'Inicio',
        icon: 'home',
        to: '/',
      },
      {
        title: 'Usuarios',
        icon: 'people',
        to: { name: 'dashboard-users' },
      },
    ],
  }),
  mounted() {
  },
  computed: {
    ...mapState({
      titleApp: state => state.app.titleApp,
    }),
  },
};
</script>
