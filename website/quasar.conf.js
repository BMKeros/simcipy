// Configuration for your app
// https://quasar.dev/quasar-cli/quasar-conf-js
const fs = require('fs');

module.exports = function (ctx) {
  return {
    // app boot file (/src/boot)
    // --> boot files are part of "main.js"
    boot: [
      'axios'
    ],
    
    css: [
      'app.styl'
    ],

    extras: [
      // 'ionicons-v4',
      // 'mdi-v3',
      'fontawesome-v5',
      // 'eva-icons',
      // 'themify',
      // 'roboto-font-latin-ext', // this or either 'roboto-font', NEVER both!

      'roboto-font', // optional, you are not bound to it
      'material-icons', // optional, you are not bound to it
    ],

    framework: {
      // iconSet: 'ionicons-v4',
      // lang: 'de', // Quasar language

      // all: true, // --- includes everything; for dev only!

      components: [
        'QLayout',
        'QHeader',
        'QDrawer',
        'QPageContainer',
        'QPage',
        'QToolbar',
        'QToolbarTitle',
        'QBtn',
        'QIcon',
        'QList',
        'QItem',
        'QItemSection',
        'QItemLabel',
        'QScrollArea',
        'QAvatar',
        'QImg',
        'QTable',
        'QBadge',
        'QBreadcrumbs',
        'QBreadcrumbsEl',
        'QSpace',
      ],

      directives: [
        'Ripple'
      ],

      // Quasar plugins
      plugins: [
        'Notify',
      ]
    },

    supportIE: false,

    build: {
      publicPath: '/static/website',
      distDir: './static/website',
      scopeHoisting: true,
      // vueRouterMode: 'history',
      // vueCompiler: true,
      // gzip: true,
      // analyze: true,
      // extractCSS: false,
      extendWebpack (cfg) {
        cfg.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /node_modules/
        })
      },
      afterBuild() {
        fs.copyFileSync(__dirname + '/static/website/index.html', __dirname + '/templates/index.html');
      }
    },

    devServer: {
      // https: true,
      port: 8001,
      open: false // opens browser window automatically
    },

    // animations: 'all', // --- includes all animations
    animations: [],
  }
}
