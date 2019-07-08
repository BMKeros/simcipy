import axios from 'axios';
import { Notify } from 'quasar';
import config from '../config';

const axiosApi = axios.create({
  baseURL: config.env === 'development' ? config.api.development : config.api.production,
});

const createNotifyError = (error) => {
  const { response } = error;

  if (response) {
    Notify.create({
      message: `[${response.status}] ${response.statusText}`,
      color: 'red',
      position: 'bottom-right',
      icon: 'report_problem',
      actions: [
        { label: 'Close', handler: () => {} },
      ],
    });
  }
};

export default class Api {
  static get(url, params) {
    return axiosApi.get(url, params).catch(createNotifyError);
  }

  static post(url, data, extra) {
    return axiosApi.post(url, data, extra).catch(createNotifyError);
  }

  static patch(url, data, extra) {
    return axiosApi.patch(url, data, extra).catch(createNotifyError);
  }

  static put(url, data, extra) {
    return axiosApi.put(url, data, extra).catch(createNotifyError);
  }

  static delete(url, extra) {
    return axiosApi.delete(url, extra).catch(createNotifyError);
  }
}
