void Ex_2_4() {
    double u, theta, phi;
    auto gen = new TRandom();
    gen->SetSeed(69);
    std::ofstream fOut;
    fOut.open("Ex_2_4.dat");
    for(int i = 0; i < 100; ++i) {
        u = gen->Uniform(0., 1.);
        theta = TMath::ACos(2*u - 1);
        u = gen->Uniform(0., 1.);
        phi = 2*TMath::Pi()*u;
        fOut << theta << '\t' << phi << '\n';
    }
    fOut.close();
}