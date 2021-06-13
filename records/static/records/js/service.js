class ApiService {
    constructor() {
        this.instance = axios.create({
        })
    }

    setHeader(token) {
        this.instance.defaults.headers.common.Authorization = `Token ${token}`
    }

    removeHeader() {
        this.instance.defaults.headers.common = {}
    }

    request(method, url, data = {}, config = {}) {
        return this.instance({
            method,
            url,
            data,
            ...config
        })
    }

    get(url, config = {}) {
        return this.request('GET', url, {}, config)
    }

    post(url, data, config = {}) {
        return this.request('POST', url, data, config)
    }

    put(url, data, config = {}) {
        return this.request('PUT', url, data, config)
    }

    patch(url, data, config = {}) {
        return this.request('PATCH', url, data, config)
    }

    delete(url, data = {}, config = {}) {
        return this.request('DELETE', url, data, config)
    }
}

class RecordService {
    constructor() {
        this.request = new ApiService()
    }

    getRecordList(config={}) {
        return this.request.get('/api/v2/record', config)
    }

    createRecord(data) {
        return this.request.post('/api/v2/record/', data)
    }

    updateRecord(projectId, payload) {
        return this.request.patch(`/api/v2/record/${projectId}/`, payload)
    }

    deleteRecord(projectId) {
        return this.request.delete(`/api/v2/record/${projectId}/`)
    }

    fetchRecordById(projectId) {
        return this.request.get(`/api/v2/record/${projectId}/`)
    }

}

