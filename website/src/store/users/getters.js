import * as typesUser from './types';

export default {
  [typesUser.GET_USERS](state) {
    return state.users;
  },
};
