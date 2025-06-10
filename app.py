import streamlit as st
from data_preprocessing import preprocess_input
from prediction import predict_dropout

st.title("🎓 Prediksi Risiko Dropout Mahasiswa")

st.info("📝 Aplikasi ini menggunakan 22 faktor utama untuk memprediksi risiko dropout mahasiswa")

# Create three columns for better layout
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📋 Data Pribadi")

    scholarship_holder = st.selectbox("🎯 Penerima Beasiswa",
                                    options=[0, 1],
                                    format_func=lambda x: "Tidak" if x == 0 else "Ya")

    gender = st.selectbox("👤 Jenis Kelamin",
                         options=[1, 0],
                         format_func=lambda x: "Laki-laki" if x == 1 else "Perempuan")

    application_order = st.selectbox("📝 Urutan Pilihan Program",
                                   options=[0, 1, 2, 3, 4, 5, 6, 9],
                                   format_func=lambda x: f"Pilihan ke-{x+1}" if x < 6 else f"Pilihan ke-{x+1}")

    debtor = st.selectbox("💳 Status Hutang",
                         options=[0, 1],
                         format_func=lambda x: "Tidak Berhutang" if x == 0 else "Berhutang")

    displaced = st.selectbox("🏠 Status Pengungsi",
                           options=[0, 1],
                           format_func=lambda x: "Tidak" if x == 0 else "Ya")

    tuition_up_to_date = st.selectbox("💰 Status Pembayaran SPP",
                                    options=[1, 0],
                                    format_func=lambda x: "Lunas" if x == 1 else "Belum Lunas")

    marital_status = st.selectbox("❤️ Status Pernikahan",
                                 options=[1, 2, 3, 4, 5, 6],
                                 format_func=lambda x: f"Status {x}")

    application_mode = st.selectbox("📝 Mode Aplikasi",
                                   options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 26, 27, 42, 43, 44, 51, 53, 57],
                                   format_func=lambda x: f"Mode {x}")

    daytime_evening_attendance = st.selectbox("⏰ Waktu Kuliah",
                                             options=[1, 0],
                                             format_func=lambda x: "Siang" if x == 1 else "Malam")

with col2:
    st.subheader("🎓 Data Akademik")

    previous_qualification = st.selectbox("🎓 Kualifikasi Sebelumnya",
                                        options=[1, 2, 3, 4, 5, 6, 9, 10, 12, 14, 15, 19, 38, 39, 40, 42, 43],
                                        format_func=lambda x: f"Kualifikasi {x}")

    course = st.selectbox("📚 Program Studi",
                         options=[33, 171, 8014, 9003, 9070, 9085, 9119, 9130, 9147, 9238, 9254, 9500, 9556, 9670, 9773, 9853, 9991],
                         format_func=lambda x: f"Program {x}")

    previous_qualification_grade = st.number_input("💯 Nilai Kualifikasi Sebelumnya", min_value=0.0, max_value=200.0, value=120.0)

    nationality = st.selectbox("🌍 Kebangsaan",
                                options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
                                format_func=lambda x: f"Kebangsaan {x}")

    mothers_qualification = st.selectbox("👩‍🎓 Kualifikasi Ibu",
                                        options=[1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44],
                                        format_func=lambda x: f"Kualifikasi {x}")

    fathers_qualification = st.selectbox("👨‍🎓 Kualifikasi Ayah",
                                        options=[1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44],
                                        format_func=lambda x: f"Kualifikasi {x}")

    mothers_occupation = st.selectbox("👩‍💼 Pekerjaan Ibu",
                                     options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                     format_func=lambda x: f"Pekerjaan {x}")

with col3:
    st.subheader("📊 Data Ekonomi & Lainnya")

    fathers_occupation = st.selectbox("👨‍💼 Pekerjaan Ayah",
                                     options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                     format_func=lambda x: f"Pekerjaan {x}")

    admission_grade = st.number_input("💯 Nilai Masuk", min_value=0.0, max_value=200.0, value=125.0)

    educational_special_needs = st.selectbox("📚 Kebutuhan Pendidikan Khusus",
                                            options=[0, 1],
                                            format_func=lambda x: "Tidak" if x == 0 else "Ya")

    age_at_enrollment = st.number_input("🎂 Usia Saat Mendaftar", min_value=17, max_value=70, value=20)

    international = st.selectbox("🌍 Status Internasional",
                                options=[0, 1],
                                format_func=lambda x: "Tidak" if x == 0 else "Ya")

    curricular_units_1st_sem_credited = st.number_input("📚 Kredit Semester 1", min_value=0, max_value=30, value=6)

    gdp = st.selectbox("📈 GDP (%)",
                      options=[3.51, 2.02, 1.79, 1.74, 0.79, 0.32, -0.92, -1.7, -3.12, -4.06])

    unemployment = st.selectbox("📉 Tingkat Pengangguran (%)",
                              options=[7.6, 8.9, 9.4, 10.8, 11.1, 12.4, 12.7, 13.9, 15.5, 16.2])

# Add some spacing
st.markdown("---")

# Prediction button
if st.button("🔍 Prediksi Risiko Dropout", type="primary", use_container_width=True):
    # Create complete input data with default values for all 22 features
    input_data = {
        "Scholarship_holder": scholarship_holder,
        "Gender": gender,
        "Application_order": application_order,
        "Debtor": debtor,
        "Displaced": displaced,
        "Tuition_fees_up_to_date": tuition_up_to_date,
        "Marital_status": marital_status,
        "Application_mode": application_mode,
        "Daytime_evening_attendance": daytime_evening_attendance,
        "Previous_qualification": previous_qualification,
        "Course": course,
        "Previous_qualification_grade": previous_qualification_grade,
        "Nacionality": nationality,
        "Mothers_qualification": mothers_qualification,
        "Fathers_qualification": fathers_qualification,
        "Mothers_occupation": mothers_occupation,
        "Fathers_occupation": fathers_occupation,
        "Admission_grade": admission_grade,
        "Educational_special_needs": educational_special_needs,
        "Age_at_enrollment": age_at_enrollment,
        "International": international,
        "Curricular_units_1st_sem_credited": curricular_units_1st_sem_credited,
        "GDP": gdp,
        "Unemployment_rate": unemployment,
    }

    try:
        with st.spinner("🔄 Memproses prediksi..."):
            # Process input and make prediction
            processed_input = preprocess_input(input_data)
            prediction = predict_dropout(processed_input)

        # Display results with enhanced styling
        st.markdown("---")
        st.subheader("📊 Hasil Prediksi:")

        if prediction == 1:
            st.error("⚠️ **RISIKO TINGGI DROPOUT**")

            # Show risk factors
            st.markdown("### 🔍 **Faktor Risiko Teridentifikasi:**")
            risk_factors = []
            if debtor == 1:
                risk_factors.append("💳 Status berhutang")
            if tuition_up_to_date == 0:
                risk_factors.append("💰 SPP belum lunas")
            if displaced == 1:
                risk_factors.append("🏠 Status pengungsi")
            if unemployment > 12:
                risk_factors.append("📉 Tingkat pengangguran tinggi")
            if gdp < 0:
                risk_factors.append("📈 Kondisi ekonomi menurun")

            if risk_factors:
                for factor in risk_factors:
                    st.markdown(f"- {factor}")
            else:
                st.markdown("- Tidak ada faktor risiko spesifik yang teridentifikasi dari data yang diberikan.")

            st.markdown("### 💡 **Rekomendasi:**")
            st.warning("""
            - 🎯 **Konsultasi dengan pembimbing akademik**
            - 💰 **Cari informasi program bantuan keuangan**
            - 📚 **Ikuti program bimbingan belajar**
            - 🤝 **Bergabung dengan komunitas mahasiswa**
            - 📞 **Komunikasi rutin dengan keluarga**
            """)

        else:
            st.success("✅ **RISIKO RENDAH DROPOUT**")

            # Show positive factors
            st.markdown("### 🌟 **Faktor Pendukung:**")
            positive_factors = []
            if scholarship_holder == 1:
                positive_factors.append("🎯 Penerima beasiswa")
            if tuition_up_to_date == 1:
                positive_factors.append("💰 SPP lunas")
            if debtor == 0:
                positive_factors.append("💳 Tidak berhutang")
            if displaced == 0:
                positive_factors.append("🏠 Status tempat tinggal stabil")

            if positive_factors:
                for factor in positive_factors:
                    st.markdown(f"- {factor}")
            else:
                st.markdown("- Tidak ada faktor pendukung spesifik yang teridentifikasi dari data yang diberikan.")

            st.markdown("### 💡 **Tips Mempertahankan Performa:**")
            st.info("""
            - 📈 **Pertahankan motivasi belajar**
            - ⏰ **Kelola waktu dengan baik**
            - 🎯 **Tetap fokus pada tujuan akademik**
            - 🤝 **Jaga hubungan baik dengan dosen**
            - 🏃‍♂️ **Jaga keseimbangan hidup**
            """)

    except Exception as e:
        st.error(f"❌ **Terjadi kesalahan:** {str(e)}")
        st.info("💡 Pastikan semua data telah diisi dengan benar dan coba lagi.")

# Sidebar with information
with st.sidebar:
    st.markdown("## ℹ️ Tentang Aplikasi")
    st.info("""
    **Prediksi Dropout Mahasiswa**

    Aplikasi ini menggunakan Gradient Boosting untuk memprediksi risiko dropout berdasarkan:

    🔹 **Data Pribadi:** Gender, status beasiswa, dll.
    🔹 **Data Akademik:** Program studi, kualifikasi
    🔹 **Data Ekonomi:** GDP, tingkat pengangguran
    🔹 **Data Finansial:** Status hutang, pembayaran SPP
    """)

    st.markdown("## 📊 Statistik")
    st.metric("Features Used", "22")  # Updated to 22
    st.metric("Accuracy", "~74%")

    st.markdown("## ⚠️ Disclaimer")
    st.warning("""
    Hasil prediksi ini hanya sebagai **panduan** dan tidak menggantikan penilaian akademik resmi.
    """)
