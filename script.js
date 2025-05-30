function getRandomBirthdays(count) {
    const birthdays = [];
    for (let i = 0; i < count; i++) {
        const day = Math.floor(Math.random() * 365);
        const date = new Date(2022, 0);
        date.setDate(date.getDate() + day);
        birthdays.push(date);
    }
    return birthdays;
}

function hasMatchingBirthday(birthdays) {
    const formatted = birthdays.map(d => d.toDateString());
    const counts = formatted.reduce((acc, date) => {
        acc[date] = (acc[date] || 0) + 1;
        return acc;
    }, {});
    for (let date in counts) {
        if (counts[date] > 1) {
            return { match: true, date, count: counts[date] };
        }
    }
    return { match: false };
}

function runSimulation() {
    const count = parseInt(document.getElementById("peopleCount").value);
    const resultDiv = document.getElementById("result");

    if (count > 1000) {
        resultDiv.innerHTML = `<p style="color: darkred;"><strong>Ошибка:</strong> Максимум — 1000 человек. Уменьшите значение.</p>`;
        return;
    }

    const birthdays = getRandomBirthdays(count);
    const result = hasMatchingBirthday(birthdays);

    const formatted = birthdays
        .map(d => d.toLocaleDateString('ru-RU', { month: 'short', day: 'numeric' }))
        .join(', ');

    let html = `<p><strong>Сгенерированные дни рождения:</strong><br>${formatted}</p>`;
    if (result.match) {
        html += `<p style="color: crimson;"><strong>Совпадение!</strong> ${result.count} человек родились <em>${new Date(result.date).toLocaleDateString('ru-RU', { month: 'short', day: 'numeric' })}</em>.</p>`;
    } else {
        html += `<p style="color: green;"><strong>Совпадений нет.</strong> Все дни рождения разные.</p>`;
    }

    resultDiv.innerHTML = html;
}
