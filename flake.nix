{
  description = "Basic Python Environment using poetry2nix";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.11";
    utils.url = "github:numtide/flake-utils";
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, utils, poetry2nix}: (utils.lib.eachSystem ["x86_64-linux" ] (system:
    let
      pkgs = import nixpkgs {
        inherit system;
        config.cudaSupport = true;
        config.allowUnfree = true;
        overlays = [
          poetry2nix.overlays.default
        ];
      };
      pypkgs-build-requirements = {
        petl = [ "setuptools" ];
        # attrs = [ "hatchling" ];
        # urllib3 = [ "hatchling" ];
        # hbreader = [ "setuptools" ];
        # pytrie = [ "setuptools" ];
        # url-normalize = [ "poetry-core" ];
        # cfgraph = [ "setuptools" ];
        # pytest-logging = [ "setuptools" ];
        # mkdocs-windmill = [ "setuptools" ];
        # paginate = [ "setuptools" ];
      };

      p2n-overrides = pkgs.poetry2nix.defaultPoetryOverrides.extend (self: super:
        builtins.mapAttrs (package: build-requirements:
          (builtins.getAttr package super).overridePythonAttrs (old: {
            buildInputs = (old.buildInputs or [ ]) ++ (builtins.map (pkg: if builtins.isString pkg then builtins.getAttr pkg super else pkg) build-requirements);
          })
        ) pypkgs-build-requirements
      );

      args = {
        projectDir = ./.;
        preferWheels = true;
        overrides = p2n-overrides;
      };
      env = pkgs.poetry2nix.mkPoetryEnv args;
      app = pkgs.poetry2nix.mkPoetryApplication args;
   in
     rec {
       ## See https://github.com/nix-community/poetry2nix/issues/1433
       ## It seems like poetry2nix does not seem to install as dev
       ## environment
       ## devShells.default = env.env;
       devShells.default = pkgs.mkShell {
         packages = [ env ];
         shellHook = ''
            export PYTHONPATH=$PWD
         '';
       };
       packages.basic = app;
       packages.default = self.packages.${system}.basic;
      }
    )
  );
}
