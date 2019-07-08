import { LOAD_USERS } from './types';

export default {
  [LOAD_USERS](state, payload) {
    state.users = payload;
  },
};
