export default {
    data() {
        return {
            email_login: '',
            password_login: '',
            login_errors: '',

            username: '',
            phone_number: '',
            email: '',
            password: '',

            register_errors: ''
        }
    },
    emits: ['login'],
    methods: {
        async submit(e) {
            const request_options = {
                method: "POST",
                headers: { "Content-Type" : "application/json" },
                body: JSON.stringify({
                    "username": this.username,
                    "phone_number": this.phone_number,
                    "email": this.email,
                    "password": this.password
                })
            };
            const res = await fetch('/api/auth/users/', request_options)
            const resj = await res.json()

            if (res['status'] != 201) {
                this.register_errors = Object.values(resj)
                return;
            }
            
            const token_options = {
                method: "POST",
                headers: { "Content-Type" : "application/json" },
                body: JSON.stringify({
                    "email": this.email,
                    "password": this.password
                })
            };
            const token_res = await fetch('/api/auth/token/login/', token_options)
            const tokenj = await token_res.json()
            window.localStorage.setItem('access_token', tokenj['auth_token'])
            this.$emit('login', true)
            this.$router.push('/')
        },
        async login_submit(e) {
            const token_options = {
                method: "POST",
                headers: { "Content-Type" : "application/json" },
                body: JSON.stringify({
                    "email": this.email_login,
                    "password": this.password_login
                })
            };
            const res = await fetch('/api/auth/token/login/', token_options)
            const resj = await res.json()

            if (res['status'] != 200) {
              this.login_errors = Object.values(resj)
              return;
            }

            window.localStorage.setItem('access_token', resj['auth_token'])
            this.$emit('login', true)
            this.$router.push('/')
        }
    },
    template: `
    <form @submit.prevent="login_submit" ref="loginForm">
      <h2 class="display-6">Вход</h2>
      <div v-if="login_errors">
        <div v-for="error in login_errors" :key="error.id">
          <small v-for="e in error" :key="e.id" class="text-primary">{{ e }}<br></small>
        </div>
      </div>
      <input id="email_login" v-model="email_login" type="email" class="form-control mb-2" placeholder="Почта" required>
      <input id="password_login" v-model="password_login" type="password" class="form-control mb-4" placeholder="Пароль" required>
      <input type="submit" class="form-control btn btn-outline-info mb-5" value="Войти">
    </form>

    <form @submit.prevent="submit" ref="registerForm">
      <h2 class="display-6">Нет учётки? Зарегистрируйтесь!</h2>
      <div v-if="register_errors">
        <div v-for="error in register_errors" :key="error.id">
          <small v-for="e in error" :key="e.id" class="text-primary">{{ e }}<br></small>
        </div>
      </div>
      <input v-model="username" class="form-control mb-2" placeholder="Имя" ref="username" id="username" required>
      <input v-model="phone_number" type="tel" class="form-control mb-2" placeholder="Телефон" ref="phone_number" required>
      <input v-model="email" type="email" class="form-control mb-2" placeholder="Почта" ref="email" required>
      <input v-model="password" type="password" class="form-control mb-4" placeholder="Пароль" ref="password" required>
      <input type="submit" class="form-control btn btn-outline-info" value="Зарегистрироваться">
    </form>
    `
}