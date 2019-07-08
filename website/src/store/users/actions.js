import Api from '../../services/apiService';
import * as typesUser from './types';


export default {
  [typesUser.LOAD_USERS]({ commit }) {
    Api.get('/users/?id=1').then((response) => {
      commit(typesUser.LOAD_USERS, response);
    });
  },
};
