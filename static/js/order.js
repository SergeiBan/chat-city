export default {
    data() {
        return {
            title: 'Оставьте заявку и мы свяжемся в течении дня!',
            category: '',
            part: '',
            description: '',
            phone_number: '',
            phone_number_placeholder: 'Телефон',
            email: ''
        }
    },
    methods: {
        async submit() {
            const res = await fetch(
                '/api/orders/',
                {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 
                    part: this.part,
                    phone_number: this.phone_number,
                    category: this.category,
                    description: this.description == '' ? null : this.description,
                    email: this.email == '' ? null : this.email
                })
            });
            const resj = await res.json()
            let isCorrect = true
            for (const [k, v] of Object.entries(resj)) {
                if (Array.isArray(v)) {
                    isCorrect = false
                    this[k] = ''
                    this[`${k}_placeholder`] = `${v[0]}`
                }
            }
            if (isCorrect) {
                this.$refs.orderForm.reset();
                this.title = 'Спасибо! Оставите новую заявку?'
            }
        }
    },
    template: `
    <form @submit.prevent="submit" ref="orderForm">
        <h1 class="display-6 h-25">{{ title }}</h1>

        <select v-model="category" class="form-control mb-2" required>
          <option value="" disabled selected>Выберите категорию техники</option>
          <option value="agro">Сельскохозяйственная техника</option>
          <option value="forestry">Лесозаготовительная техника</option>
          <option value="construction">Строительная техника</option>
        </select>

        <input v-model="part" type="text" id="part-field" name="part" class="form-control mb-2" placeholder="Укажите артикул запчасти" required ref="part">
        
        <input v-model="phone_number" type="tel" id="tel-field" name="tel"
        class="form-control mb-2" :placeholder="phone_number_placeholder" required>
        
        <input v-model="email" type="email" id="email-field" name="email" class="form-control mb-2" placeholder="Необязательно. Почта" ref="email">
        
        <textarea v-model="description" placeholder="Необязательно. Примечания" cols="10" rows="5" id="description-field" name="description"
        class="form-control mb-4" style="resize:none;" ref="description"></textarea>

        <input type="submit" name="submit" value="Подать заявку"
        class="form-control mb-2 btn btn-outline-info">

      </form>
    `
}